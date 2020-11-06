
def initialize_routes(api):
    api.add_resource(Bank, '/')

    api.add_resource(Customer, '/api/accountdetail','/api/accountdetail/<string:username>')
    api.add_resource(Login, '/api/accountdetail/login')
    api.add_resource(Loan, '/api/loans')
