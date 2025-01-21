import yaml

config_file = open('config/company_config.yml', 'r', encoding='utf-8')
company_config = yaml.safe_load(config_file)
config_file.close()

valid_regnums = {}
regnums_file = open('config/registration_numbers.yml', 'r', encoding='utf-8')

for methodic, regnums in yaml.safe_load(regnums_file).items():
    for regnum in regnums:
        valid_regnums[regnum] = methodic

regnums_file.close()
