from os.path import join, dirname
import yaml

class Context():
    '''
    Classe que possui todas as configurações nescessárias para captura dos dados das receitas
    '''
    def __init__(self):
        self._conf = self._read_config()
        self.steps = self._read_steps()
        # self.runs = self._create_runs()

        self.local_files = self._get_config('LOCAL_FILES')
        self.dir_saida = join(self.local_files,self._get_config('DIR_SAIDA'))
        self.dir_fetcher = join(self.local_files,self._get_config('DIR_FETCHER'))

        self.dir_webdriver = self._get_config('DIR_WEBDRIVER')

        self.dir_sql = join(self.local_files,self._get_config('DIR_SQL'))
        self.user_sql = self._get_config('USER_SQL')
        self.password_sql = self._get_config('PASSWORD_SQL')
        self.database_sql = self._get_config('DATABASE_SQL')
        self.dbname_sql = self._get_config('DBNAME_SQL')
        self.host_sql = self._get_config('HOST_SQL')
        self.port_sql = self._get_config('PORT_SQL')


    def _read_config(self):
        with open(join(dirname(__file__),"configuration.yml"), 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def _get_config(self, attribute):
        if attribute:
            try:
                return self._conf[attribute]
            except:
                return None

    def _read_steps(self):
        with open(join(dirname(__file__),"steps.yml"), 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def _create_runs(self):
        runs = {}

        for step in self.steps.keys():
            runs[step] = 0
            for dep in self.steps[step] .keys():
                runs[dep] = 0

        return runs



