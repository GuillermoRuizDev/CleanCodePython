import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    def serialize(self, serializer):
        serializer.start_object('song', self.song_id)
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)


""" class SongSerializer:
    def serialize(self, song, format):
        serializer= self.get_serializer(format)
        return serializer(song)

    def get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    def _serialize_to_json(self, song):
        song_info = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(song_info)

    def _serialize_to_xml(self, song):
        song_info = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_info, 'title')
        title.text = song.title
        artist = et.SubElement(song_info, 'artist')
        artist.text = song.artist
        return et.tostring(song_info, encoding='unicode') """