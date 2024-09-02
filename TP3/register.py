class Envio:
    def __init__ (self,codpos,address,id_ts,wp):
        self.cod_pos = codpos,
        self.address = address       
        self.type_shipment = id_ts    
        self.waypay = wp

    def __str__(self):
        text = f""" {str(self.cod_pos)} - {str(self.address)} - {self.type_shipment} - {self.waypay} """
        return text

class DataShipment:
    def __init__ (self,cost_ship,va,co_sh,pr_sh):
        self.cost_shipment = cost_ship,
        self.valid_address = va,
        self.country_shipment = co_sh,
        self.province_shipment = pr_sh

    def __str__(self):
        text = f""" {self.cost_shipment} - {bool(self.valid_address)} - {str(self.country_shipment)} - {str(self.province_shipment)} """
        return text