import click
import yaml

def kernel(config):
    from pygate.predefined.simulations import  make_simulation
    if config is not None:
        with open(config) as fin:
            c = yaml.load(fin)
    else:
        c = {}
    mac=make_simulation('OpticalSystem').render()
    return mac

@click.command()
@click.option('--config', '-c', help="mac maker config.", default=None)
@click.option('--output', '-o', help="output mac filename", default="main.mac")
def cli(config, output):
    content = kernel(config)
    with open(output, 'w') as fout:
        print(content, file=fout)

if __name__ == '__main__':
    cli()


