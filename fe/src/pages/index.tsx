import Billboard from "@/components/Billboard";
import MovieList from "@/components/MovieList";
import Navbar from "@/components/Navbar";
import useCurrentUser from "@/hooks/useCurrentUser";
import useFavorites from "@/hooks/useFavorites";
import useMovies from "@/hooks/useMovieList";
import { NextPage } from "next";
import { getSession } from "next-auth/react";

export async function getServerSideProps(context: NextPage) {
  const session = await getSession(context);

  if (!session) {
    return {
      redirect: {
        destination: "/auth",
        permanent: false,
      },
    };
  }

  return {
    props: {},
  };
}

export default function Home() {
  const { data: movies = [] } = useMovies();
  const { data: favorites = [] } = useFavorites();

  const { data: currentUser, mutate } = useCurrentUser();
  console.log("currentUser is", currentUser);


  return (
    <>
      <Navbar />
      <Billboard />
      <div className="pb-40">
        <MovieList title="Trending Now" data={movies} />
        <MovieList title="My List" data={favorites} />
      </div>
    </>
  );
}
