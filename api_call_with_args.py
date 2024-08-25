import datetime
import urllib3
import click


@click.option('--accountId', required=True, help='define account ID', type=str)
@click.command()

def run_Script( accountId):

    http = urllib3.PoolManager()
    home = 'http://localhost:64830/'

    
    print('Starting...')

    url = home + 'api/Accounts/Get' + '?accountId=' + accountId
    
    print(url)
    r1 = http.request('GET', url)

    print(' Result: ' + str(r1.status) + ' ' +
            r1.data.decode('utf-8') + r1.geturl())


if __name__ == '__main__':
    run_Script()
