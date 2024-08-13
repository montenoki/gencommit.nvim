import pynvim


@pynvim.plugin
class ExPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.cfg = nvim.exec_lua('return require("example_plugin").getConfig()')

    @pynvim.function("ExPlugEcho", sync=True)
    def echo(self, args):
        self.nvim.command(f"echomsg 'From config: {self.cfg['path']}'")
