class Config:
  '''
  contains configuarations for all stages of the application
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://emmanuel:lilfranken@localhost/blogpost'
class ProdConfig(Config):
  '''
  contains configuarations for production stage
  '''
  pass
class DevConfig(Config):
  '''
  contains configuarations for developments stage
  '''
  DEBUG=True
config_options={
  'development' : DevConfig,
  'production'  :ProdConfig
}
