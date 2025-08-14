def _lock_single_type_tracks(dvr, track_type, status):
    for track in range(dvr.tl().GetTrackCount(track_type)):
        dvr.tl().SetTrackLock(track_type, track + 1, status)


def lock_all_tracks(dvr, track_type):
    if track_type:
        _lock_single_type_tracks(dvr, track_type, True)
    else:
        _lock_single_type_tracks(dvr, 'subtitle', True)
        _lock_single_type_tracks(dvr, 'video', True)
        _lock_single_type_tracks(dvr, 'audio', True)


def unlock_all_tracks(dvr, track_type):
    if track_type:
        _lock_single_type_tracks(dvr, track_type, False)
    else:
        _lock_single_type_tracks(dvr, 'subtitle', False)
        _lock_single_type_tracks(dvr, 'video', False)
        _lock_single_type_tracks(dvr, 'audio', False)


def lock_tracks(dvr, track_type, start_track, end_track):
    for track in range(start_track, end_track + 1):
        dvr.tl().SetTrackLock(track_type, track, True)


def unlock_tracks(dvr, track_type, start_track, end_track):
    for track in range(start_track, end_track + 1):
        dvr.tl().SetTrackLock(track_type, track, False)


def delete_tracks(dvr, track_type, start_track, end_track):
    for track in range(start_track, end_track + 1):
        dvr.tl().DeleteTrack(track_type, start_track)


def delete_all_tracks(dvr, track_type):
    if track_type == 'video':
        dvr.tl().AddTrack(track_type)
    elif track_type == 'audio':
        dvr.tl().AddTrack(track_type, 'stereo')
    for track in range(dvr.tl().GetTrackCount(track_type) - 1):
        dvr.tl().DeleteTrack(track_type, 1)


def append_to_timeline(dvr, item, media_type, track_index, start_tc, end_tc, record_tc):
    item_info = {"mediaPoolItem": item}

    if media_type == 'video':
        item_info["mediaType"] = 1
    elif media_type == 'audio':
        item_info["mediaType"] = 2
    elif media_type == 1:
        item_info["mediaType"] = 1
    elif media_type == 2:
        item_info["mediaType"] = 2

    if track_index is not None:
        item_info["trackIndex"] = track_index

    if start_tc is not None:
        if type(start_tc) is int:
            item_info["startFrame"] = start_tc
        elif type(start_tc) is str:
            item_info["startFrame"] = dvr.timecode_to_frames(start_tc)

    if end_tc is not None:
        if type(end_tc) is int:
            if end_tc < 0:
                item_info["endFrame"] = int(item.GetClipProperty('End')) - end_tc
            else:
                item_info["endFrame"] = end_tc
        elif type(end_tc) is str:
            if end_tc[0] == '-':
                item_info["endFrame"] = int(item.GetClipProperty('End')) - dvr.timecode_to_frames(end_tc[1:])
            else:
                item_info["endFrame"] = dvr.timecode_to_frames(end_tc)

    if record_tc is not None:
        if type(record_tc) is int:
            item_info["recordFrame"] = record_tc
        elif type(record_tc) is str:
            item_info["recordFrame"] = dvr.timecode_to_frames(record_tc)

    dvr.mdp().AppendToTimeline([item_info])
