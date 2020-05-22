from .Interceptor import Interceptor

class TotalInterceptor(Interceptor):
    def __intit__(self):
        print("Intercepting....")

    def update(self, totalcontext):
        user = totalcontext.getUser()
        total = totalcontext.getTotal()
        print(str(user) + ',' + str(total))
        try:
            with open('log.txt', 'a') as log:
                    log.write("\n")
                    log.write(str(user) + ',' + str(total))
        except Exception as e:
            print(e)