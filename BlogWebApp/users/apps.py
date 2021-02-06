from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #register signal 
    def ready(self):
        import users.signals
    