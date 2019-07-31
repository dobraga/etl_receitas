import os

class Fetcher():
    def __init__(self, ctx, entity):
        self.dir_webdriver = ctx.dir_webdriver
        self.dir_fetcher = ctx.dir_fetcher
        self.dir_saida = ctx.dir_saida

        self.cmd = self.create_cmd(entity)

        self.execute()

    def create_cmd(self, entity):
        return "scrapy runspider {dir_fetcher}/{entity}.py -a OUTPUT_FILE={dir_saida}/{entity}.csv -a DIR_WEBDRIVER={dir_web}".format(
            dir_web = self.dir_webdriver,
            dir_fetcher = self.dir_fetcher,
            dir_saida = self.dir_saida,
            entity = entity)

    def execute(self):
        try:
            os.system(self.cmd)
            return True
        except:
            return False


    