import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";
import { useRef } from "@odoo/owl";

patch(PaymentScreen.prototype, {
    setup() {
        super.setup();
        this.congratTxt = useRef("congrat_txt");
    },
    onChangeCongrat() {
        this.pos.config.congratulatory_text = this.congratTxt.el.value
    }

})