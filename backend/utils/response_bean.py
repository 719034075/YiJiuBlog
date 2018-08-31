class ResponseBean:
    success = False
    message = ''
    data = {}

    def get_success_instance(self):
        self.success = True
        self.message = ''
        self.data = {}
        return self

    def get_fail_instance(self):
        self.success = False
        self.message = ''
        self.data = {}
        return self

