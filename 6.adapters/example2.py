class Target:
    def request(self) -> str:
        return 'Target: The default target\'s behavior'


class Adaptee:
    def specific_request(self) -> str:
        return '.eetpadA eht fo roivaheb laicepS'


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return 'Adapter (TRANSLATED) %s' % self.specific_request()[::-1]


def client_code(target: Target) -> None:
    print(target.request())


if __name__ == '__main__':
    print('Client: I can work just fine with the Target objects:')
    target = Target()
    client_code(target)
    print()

    adaptee = Adaptee()
    print('Client: The Adaptee class has a weird interface.'
          'See, In don\'t understand it:')
    print('Adaptee: %s' % adaptee.specific_request())

    print('Client: But I can work with it via the Adapter:')
    adapter = Adapter()
    client_code(adapter)
