import click
import yaml

def kernel(config):
    from pygate.predefined.simulations import optical_gamma, simulation, PredefinedSimulations
    from pygate.predefined.sources import sphere, Vec3
    if config is not None:
        with open(config) as fin:
            c = yaml.load(fin)
    else:
        c = {}
    src_pos = Vec3(*(list(c.get('src_pos', (150.0, 0.0, 0.0)))+['mm']))
    crystal_size = Vec3(*(list(c.get('crystal_size', (30.0, 30.0, 30.0)))+['mm']))
    nb_primaries = c.get('nb_primaries', 1e6)
    mac = optical_gamma(sphere(0.1, src_pos),
                        crystal_size=crystal_size,
                        nb_primaries=nb_primaries).render()
    return mac

@click.command()
@click.option('--config', '-c', help="mac maker config.", default="mac.yml")
@click.option('--output', '-o', help="output mac filename", default="main.mac")
def cli(config, output):
    content = kernel(config)
    with open(output, 'w') as fout:
        print(content, file=fout)

if __name__ == '__main__':
    cli()
