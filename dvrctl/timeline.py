from typing import Optional, Union

class Timeline:
    def __init__(self, resolve):
        self.resolve = resolve
        self.obj = resolve.GetProjectManager().GetCurrentProject().GetCurrentTimeline()

    def __getattr__(self, name):
        """让没有在包装类中定义的属性，直接去内部对象找"""
        return getattr(self.obj, name)

    def __repr__(self):
        """print 时，显示内部对象的 repr"""
        return repr(self.obj)

    def lock_track(self, track_type:str, track:int,status:bool):
        self.obj.SetTrackLock(track_type, track, status)

    def lock_tracks(self, track_type:str, status:bool):
        for track in range(self.obj.GetTrackCount(track_type)):
            self.obj.SetTrackLock(track_type, track + 1, status)

    def delete_track(self, track_type:str, start_track:int, count:int=1):
        for track in range(count):
            self.obj.DeleteTrack(track_type, start_track)

    def delete_tracks(self, track_type:str):
        count = self.obj.GetTrackCount(track_type)
        for track in range(count):
            self.obj.DeleteTrack(track_type, 1)

    def append_to_timeline(self, item, *,
                           media_type: Optional[Union[str, int]] = None,
                           track_index: Optional[int] = None,
                           start_tc: Optional[Union[int, str]] = None,
                           end_tc: Optional[Union[int, str]] = None,
                           record_tc: Optional[Union[int, str]] = None
                           ):
        from .general import General
        from .media_pool import MediaPool

        item_info = {"mediaPoolItem": item}

        if media_type == 'video' or media_type == 1:
            item_info["mediaType"] = 1
        elif media_type == 'audio' or media_type == 2:
            item_info["mediaType"] = 2
        else:
            pass

        if track_index is not None:
            item_info["trackIndex"] = track_index

        if start_tc is not None:
            if type(start_tc) is int:
                item_info["startFrame"] = start_tc
            elif type(start_tc) is str:
                item_info["startFrame"] = General(self.resolve).tc2frames(start_tc)

        if end_tc is not None:
            if type(end_tc) is int:
                if end_tc < 0:
                    item_info["endFrame"] = int(item.GetClipProperty('End')) - end_tc
                else:
                    item_info["endFrame"] = end_tc
            elif type(end_tc) is str:
                if end_tc[0] == '-':
                    item_info["endFrame"] = int(item.GetClipProperty('End')) - General(self.resolve).tc2frames(end_tc[1:])
                else:
                    item_info["endFrame"] = General(self.resolve).tc2frames(end_tc)

        if record_tc is not None:
            if type(record_tc) is int:
                item_info["recordFrame"] = record_tc
            elif type(record_tc) is str:
                item_info["recordFrame"] = General(self.resolve).tc2frames(record_tc)
        from typing import cast, Any
        item = cast(Any, item)
        print(f'Append to timeline for {item.GetName()}, detail: {item_info}')
        return MediaPool(self.resolve).AppendToTimeline([item_info])
