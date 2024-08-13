import pynvim


@pynvim.plugin
class ExPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.cfg = nvim.exec_lua('return require("gencommit").getConfig()')

    @pynvim.function("ExPlugEcho", sync=True)
    def echo(self, args):
        self.nvim.command(f"echomsg 'From config: {self.cfg['path']}'")

    @pynvim.command("GenCommit", nargs="*", range="")
    def gen_commit_command(self, args, range):
        # 实现你的命令逻辑
        pass
