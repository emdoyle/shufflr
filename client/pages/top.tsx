import { NextPage, NextPageContext } from "next";

const TopSongs: NextPage<{
  topSongs: Record<string, string>[];
}> = ({ topSongs }) => {
  return (
    <ol>
      {topSongs.map((song) => (
        <li key={JSON.stringify(song).slice(0, 20)}>
          {song["name"] ?? "unknown name"}
        </li>
      ))}
    </ol>
  );
};

export default TopSongs;

export async function getServerSideProps(context: NextPageContext) {
  const tracks = await fetch("http://127.0.0.1:8080/top-songs/");
  const tracksJSON = await tracks.json();
  return {
    props: { topSongs: tracksJSON["items"] },
  };
}
