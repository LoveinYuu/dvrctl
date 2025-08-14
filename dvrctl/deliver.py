class Deliver:
    def __init__(self, resolve):
        self.obj = resolve

    def add_to_render(self, preset:str, path:str):
        pj = self.obj.GetProjectManager().GetCurrentProject()
        tl = pj.GetCurrentTimeline()

        if pj.LoadRenderPreset(preset):
            if pj.SetRenderSettings({"TargetDir": path}):
                job = pj.AddRenderJob()
                while job == '':
                    job = pj.AddRenderJob()
            else:
                print('\033[0;31m' + f'{tl.GetName()} Path setup failed' + '\033[0m')

        else:
            print('\033[0;31m' + f'{tl.GetName()} Preset setup failed' + '\033[0m')