from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    '''
    auth h function sthn ousia energopoiei ola ta signals opou ftia3ame emeis
    '''
    def ready(self):
        import users.signals