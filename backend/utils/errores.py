class ErrorApi(Exception):
    def __init__(self, mensaje, status_code):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.status_code = status_code
