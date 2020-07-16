import Layout from '../components/Layout';
import { useContext } from 'react';
import UserContext from '../components/UserContext';
import Link from 'next/link';

const Index = () => {

    const { recipes } = useContext(UserContext);

    return (
        <Layout>
            <h1>All My Things</h1>
            <ul>
                {recipes.map(rec => (
                    <li key={rec.id}><Link href="/recipes/[id]" as={`/recipes/${rec.id}`}><a>{rec.title}</a></Link></li>
                ))}
            </ul>

        </Layout>
    );
};

export default Index

