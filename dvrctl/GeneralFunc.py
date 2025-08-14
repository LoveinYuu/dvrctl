# 帧数转时码--------------------------------------------------------------------------------------------------------------
def frames_to_timecode(dvr, frames):
    framerate = dvr.pj().GetSetting('timelineFrameRate')
    return '{0:02d}:{1:02d}:{2:02d}:{3:02d}'.format(int(frames / (3600*framerate)),
                                                    int(frames / (60*framerate) % 60),
                                                    int(frames / framerate % 60),
                                                    int(frames % framerate))


# 时码转帧数--------------------------------------------------------------------------------------------------------------
def timecode_to_frames(dvr, timecode):
    framerate = dvr.pj().GetSetting('timelineFrameRate')
    hours, minutes, seconds, frames = map(int, timecode.split(":"))
    total_frames = (hours * 3600 + minutes * 60 + seconds) * framerate + frames
    return int(total_frames)


# 所有时间线--------------------------------------------------------------------------------------------------------------
def for_all_timelines(dvr, method):
    tl_count = dvr.pj().GetTimelineCount()
    tl_dict = {}
    for i in range(1, tl_count + 1):
        tl_dict[i] = dvr.pj().GetTimelineByIndex(i).GetName()

    tl_dict = sorted(tl_dict.items(), key=lambda x: x[1])

    for i in list(tl_dict):
        timeline = dvr.pj().GetTimelineByIndex(i[0])
        if dvr.pj().SetCurrentTimeline(timeline):
            method()
        else:
            print(f'Set Timeline:{dvr.pj().GetTimelineByIndex(i[0]).GetName()} in Project {dvr.pj().GetName()} filed')


def for_all_projects(dvr, method, all_timelines):
    from dvrctl.ProjectManagerFunc import save_project

    projects = sorted(dvr.pjm().GetProjectListInCurrentFolder())
    for project in projects:
        dvr.pjm().LoadProject(project)
        if all_timelines:
            for_all_timelines(dvr, method)
        else:
            method()

        save_project(dvr)
