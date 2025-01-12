import yaml

try:
    config_file = open('./config/company_config.local.yml')
except:
    config_file = open('./config/company_config.yml')

company_config = yaml.safe_load(config_file)
config_file.close()

valid_regnums = {}
try:
    regnums_file = open('./config/registration_numbers.local.yml')
except:
    regnums_file = open('./config/registration_numbers.yml')

for methodic, regnums in yaml.safe_load(regnums_file).items():
    for regnum in regnums:
        valid_regnums[regnum] = methodic

regnums_file.close()
