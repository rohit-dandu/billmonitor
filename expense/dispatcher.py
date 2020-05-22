class Dispatcher:
    _interceptors = []

    def register(self, interceptor):
        if interceptor not in self._interceptors:
            self._interceptors.append(interceptor)

    def unregister(self, interceptor):
        if interceptor in self._interceptors:
            self._interceptors.remove(interceptor)
    
    def dispatch(self, context):
        for interceptor in self._interceptors:
            interceptor.update(self, context)