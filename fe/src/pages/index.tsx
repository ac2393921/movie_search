import Billboard from '@/components/Billboard';
import Navbar from '@/components/Navbar';
import useCurentUser from '@/hooks/useCurrentUser';
import { NextPage } from 'next';
import { getSession } from 'next-auth/react';



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
      <Navbar />
      <Billboard />
    </>
  )
}
