import useCurrentUser from '@/hooks/useCurrentUser';
import { NextPageContext } from 'next';
import { getSession } from 'next-auth/react';
import { useRouter } from 'next/router';
import { useCallback } from 'react';
export async function getServerSideProps(context: NextPageContext) {
  const session = await getSession(context);

  if (!session) {
    return {
      redirect: {
        destination: '/login',
        permanent: false,
      },
    }
  }

  return {
    props: {},
  }
}

const profiles = () => {
  const router = useRouter();
  const {data: user} = useCurrentUser();

  const selectProfile = useCallback(() => {
    router.push('/');
  }, [router]);

  return (
    <div className="flex items-center h-full justify-center">
      <div className="flex flex-col">
        <h1 className="text-3xl md:text-6xl text-white text-center" > Who is watching?</h1>
        <div className="flex items-center justify-center gap-8 mt-10">
          <div onClick={() => router.push('/')}>
            <div className='grout flex-row w-44 mx-auto'>
              <div
                className="
                  w-44
                  h-44
                  rounded-md
                  flex
                  items-center
                  justify-center
                  border-2
                  border-transparent
                  group-hover:cursor-pointer
                  gruop-hover:border-white
                  overflow-hidden
                "
              >
                <img
                  src="/images/default-blue.png"
                  alt="Profile"
                  // className="w-full h-full object-cover"
                />
              </div>
              <div
                className="
                  mt-4
                  text-gray-400
                  text-2xl
                  text-center
                  group-hover:text-white

                "
              >
                {user?.name}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
};

export default profiles;