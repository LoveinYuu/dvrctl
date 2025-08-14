import dvrctl.DaVinciResolveScript as Bmd
from dvrctl import ProjectManagerFunc
from dvrctl import TimelineFunc
from dvrctl import DeliverFunc
from dvrctl import GeneralFunc


class GetResolve:
    def __init__(self, host=None):
        if host:
            ask_continue = input(f'The script affects on {host}, Continue?(y/n):')
            if ask_continue != 'y':
                exit()
            self.resolve = Bmd.scriptapp('Resolve', host)
            if self.resolve is None:
                print(f'\033[1;31mHost not available\033[0m')
                exit(1)
        else:
            self.resolve = Bmd.scriptapp('Resolve')

    def pjm(self):
        return self.resolve.GetProjectManager()

    def pj(self):
        return self.pjm().GetCurrentProject()

    def mdp(self):
        return self.pj().GetMediaPool()

    def tl(self):
        return self.pj().GetCurrentTimeline()

    # Project Manager Func----------------------------------------------------------------------------------------------
    def save_project(self):
        ProjectManagerFunc.save_project(self)

    # Timeline Func-----------------------------------------------------------------------------------------------------
    def lock_all_tracks(self, track_type=None):
        TimelineFunc.lock_all_tracks(self, track_type)

    def unlock_all_tracks(self, track_type=None):
        TimelineFunc.unlock_all_tracks(self, track_type)

    def lock_tracks(self, track_type, start_track, end_track):
        TimelineFunc.lock_tracks(self, track_type, start_track, end_track)

    def unlock_tracks(self, track_type, start_track, end_track):
        TimelineFunc.unlock_tracks(self, track_type, start_track, end_track)

    def delete_tracks(self, track_type, start_track, end_track):
        TimelineFunc.delete_tracks(self, track_type, start_track, end_track)

    def delete_all_tracks(self, track_type):
        TimelineFunc.delete_all_tracks(self, track_type)

    def append_to_timeline(self, item, media_type=None, track_index=None, start_tc=None, end_tc=None, record_tc=None):
        TimelineFunc.append_to_timeline(self, item, media_type, track_index, start_tc, end_tc, record_tc)

    # Deliver Func------------------------------------------------------------------------------------------------------
    def add_current_timeline_to_render(self, preset, path):
        DeliverFunc.add_current_timeline_to_render(self, preset, path)

    def add_all_timeline_to_render(self, preset, path):
        def _method():
            DeliverFunc.add_current_timeline_to_render(self, preset, path)
        GeneralFunc.for_all_timelines(self, _method)

    # General Func------------------------------------------------------------------------------------------------------
    def frames_to_timecode(self, frames):
        return GeneralFunc.frames_to_timecode(self, frames)

    def timecode_to_frames(self, timecode):
        return GeneralFunc.timecode_to_frames(self, timecode)

    def for_all_timelines(self, method):
        GeneralFunc.for_all_timelines(self, method)

    def for_all_projects(self, method, *, all_timelines=False):
        GeneralFunc.for_all_projects(self, method, all_timelines)


# 示例用法
if __name__ == "__main__":
    dvr = GetResolve()

    def name():
        print(dvr.tl().GetName())

    dvr.for_all_timelines(name)
