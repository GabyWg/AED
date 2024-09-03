class Envio:
    def __init__ (self,codpos,address,id_ts,wp,cost_ship,va,co_sh,pr_sh):
        self.cod_pos = codpos
        self.address = address
        self.type_shipment = id_ts
        self.waypay = wp
        self.cost_shipment = cost_ship
        self.valid_address = va
        self.country_shipment = co_sh
        self.province_shipment = pr_sh

    def __str__(self):
        text = self.cod_pos + ' - '
        text += self.address + ' - '
        text += ('Direccion Valida' if self.valid_address else 'Direccion Invalida') + ' - ' 
        text += str(self.type_shipment) + ' - '
        text += str(self.waypay) + ' - '
        text += str(round(self.cost_shipment,2)) + ' - '
        text += self.country_shipment + ' - '
        text += self.province_shipment
        return text
    