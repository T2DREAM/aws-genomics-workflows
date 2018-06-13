from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('getRegionMetadata', '/getRegionMetadata')
    config.add_route('getExperimentMetadata', '/getExperimentMetadata')
    config.add_route('getAnnotationRegion', '/getAnnotationRegion')
    config.add_route('getExperiment', '/getExperiment')
    config.add_route('getExperimentBigWig', '/getExperimentBigWig')
    config.add_route('getAnnotation', '/getAnnotation')
    config.add_route('getAnnotationBucket', '/getAnnotationBucket')
    config.scan()
    return config.make_wsgi_app()
