def add_current_timeline_to_render(dvr, preset, path):
    if dvr.pj().LoadRenderPreset(preset):
        if dvr.pj().SetRenderSettings({"TargetDir": path}):
            job = dvr.pj().AddRenderJob()
            while job == '':
                job = dvr.pj().AddRenderJob()
        else:
            print('\033[0;31m' + f'{dvr.tl().GetName()}输出位置设置失败' + '\033[0m')

    else:
        print('\033[0;31m' + f'{dvr.tl().GetName()}渲染预设设置失败' + '\033[0m')
