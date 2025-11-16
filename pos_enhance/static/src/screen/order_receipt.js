import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen/receipt/order_receipt";
import { patch } from "@web/core/utils/patch";
import { usePos } from "@point_of_sale/app/hooks/pos_hook";


patch(OrderReceipt.prototype, {
    setup() {
        super.setup();
        this.pos = usePos();
    }
})