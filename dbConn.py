import psycopg2


config = {'dbname': 'siliconops',
           'user': 'gaofeng.wang@wdc.com',
           'pwd': 'Gs1@wang!',
           'host': 'abo-edmprod03.cq3dszk4zmku.us-west-2.redshift.amazonaws.com',
           'port': '5439'
         }


def create_conn():
    try:
        con=psycopg2.connect(dbname=config['dbname'],
                             host=config['host'],
                             port=config['port'],
                             user=config['user'],
                             password=config['pwd'])
        return con
    except Exception as err:
        print(err)