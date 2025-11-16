import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { patch } from "@web/core/utils/patch";
import {
    BACKSPACE,
    Numpad,
    getButtons,
    DEFAULT_LAST_ROW,
    SWITCHSIGN,
} from "@point_of_sale/app/components/numpad/numpad";
import { _t } from "@web/core/l10n/translation";

// point_of_sale/**/*.xml

patch(ProductScreen.prototype, {
    setup() {
        super.setup();
    },
    getNumpadButtons() {
        const colorClassMap = {
            [this.env.services.localization.decimalPoint]: "o_colorlist_item_numpad_color_6",
            Backspace: "o_colorlist_item_numpad_color_1",
            "-": "o_colorlist_item_numpad_color_3",
        };

        const defaultLastRowValues =
            DEFAULT_LAST_ROW.map((button) => button.value) + [BACKSPACE.value];

        return getButtons(DEFAULT_LAST_ROW, [
            { value: "remove_line", text: _t("Double Delete") },
            {
                value: "discount",
                text: _t("%"),
                disabled: !this.pos.config.manual_discount || this.pos.cashier._role === "minimal",
            },
            {
                value: "price",
                text: _t("Price"),
                disabled:
                    !this.pos.cashierHasPriceControlRights() ||
                    this.pos.cashier._role === "minimal",
            },
            BACKSPACE
        ]).map((button) => ({
            ...button,
            disabled:
                button.disabled ||
                (button.value === SWITCHSIGN.value && this.pos.cashier._role === "minimal"),
            class: `
                ${defaultLastRowValues.includes(button.value) ? "" : ""}
                ${colorClassMap[button.value] || ""}
                ${this.pos.numpadMode === button.value ? "active" : ""}
                ${button.value === "quantity" ? "numpad-qty rounded-0" : ""}
                ${button.value === "price" ? "numpad-price rounded-0" : ""}
                ${button.value === "discount" ? "numpad-discount rounded-0" : ""}
            `,
        }));
    },
    onNumpadClick(buttonValue) {
        if (["quantity", "discount", "price"].includes(buttonValue)) {
            this.numberBuffer.capture();
            this.numberBuffer.reset();
            this.pos.numpadMode = buttonValue;
            return;
        }
        if (this.pos.selectedOrder.isRefund && buttonValue !== "Backspace") {
            return this.dialog.add(AlertDialog, {
                title: _t("%s update not allowed", this.pos.numpadMode),
                body: _t("You can not change the %s of the refund order.", this.pos.numpadMode),
            });
        }
        if (buttonValue === "remove_line") {
            this.numberBuffer.sendKey("Backspace");
            this.numberBuffer.sendKey("Backspace");
        } else {
            this.numberBuffer.sendKey(buttonValue);
        }
    }
})