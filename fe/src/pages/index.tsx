import useCurentUser from '@/hooks/useCurrentUser';
import { NextPage } from 'next';
import { getSession, signOut } from 'next-auth/react';


export async function getServerSideProps(context: NextPage) {
  const session = await getSession(context);

  if (!session) {
    return {
      redirect: {
        destination: '/auth',
        permanent: false
      }
    }
  }

  return {
    props: {}
  }
}


export default function Home() {
  const { data: user } = useCurentUser();
  return (
    <>
      <h1 className='text-2xl text-green-500'>Netflix Clone</h1>
      <p className='text-white'>Logged in as : {user?.email}</p>
      <button className="h-10 w-full bg-white" onClick={() => signOut()}>Logout;</button>
    </>
  )
}
