## Features

- Search Spotify for **artists**, **albums**, **songs**, and **playlists**.
- Retrieve key details like artist popularity, album release dates, and song popularity.
- Simple command-based interaction.

## Prerequisites

- Python 3.x
- Spotify API credentials (client ID and client secret) to access the Spotify API.
  
> **Note:** This script uses a custom `RequestsSession` class. Ensure your code handles authentication to set up `self.session` with the necessary access token.

## Setup

1. **Install required libraries**:
   ```bash
   pip install requests
   ```
2. **Spotify API**: Obtain Spotify API credentials from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and use them to authenticate requests.

3. **Set Environment Variables**:

## Commands

### Basic Commands

- **hello**: Displays a greeting message.
  ```bash
  >> hello
  ```
  Output: `Hello world`

- **quit**: Exits the CLI.
  ```bash
  >> quit
  ```

### Spotify API Commands

#### Search for an Artist

Searches Spotify for an artist by name, returning the artist's ID, name, popularity, and genres.

**Usage**:
```bash
>> artist <artist_name>
```

**Example**:
```bash
>> artist Coldplay
```

#### Search for an Album

Searches Spotify for an album by name, returning details like the album's ID, name, release date, popularity, total tracks, and artist names.

**Usage**:
```bash
>> album <album_name>
```

**Example**:
```bash
>> album Parachutes
```

#### Search for a Song

Searches Spotify for a song by name, returning details including song ID, name, album name, artist name(s), and popularity.

**Usage**:
```bash
>> song <song_name>
```

**Example**:
```bash
>> song Yellow
```

#### Search for a Playlist

Searches Spotify for a playlist by name, returning the playlist's ID, name, and description.

**Usage**:
```bash
>> playlist <playlist_name>
```

**Example**:
```bash
>> playlist Chill Hits
```

## Example Session

```plaintext
Welcome to Scotty's Spotify CLI
>> hello
Hello world
>> artist Coldplay
[
    {
        "id": "4gzpq5DPGxSnKTe4SA8HAU",
        "name": "Coldplay",
        "popularity": 90,
        "genres": ["alternative rock", "permanent wave", "rock"]
    }
]
>> quit
Exiting Scotty's Spotify CLI
```


## License

This CLI is intended for educational and personal use.
