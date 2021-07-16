import serializer_demo as sd
song = sd.Song('1', 'Water of Love', 'Dire Straits')
serializer = sd.SongSerializer()

print(serializer.serialize(song, 'JSON'))
#'{"id": "1", "title": "Water of Love", "artist": "Dire Straits"}'

print(serializer.serialize(song, 'XML'))
#'<song id="1"><title>Water of Love</title><artist>Dire Straits</artist></song>'

serializer.serialize(song, 'YAML')
""" Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./serializer_demo.py", line 30, in serialize
    raise ValueError(format)
ValueError: YAML """