import Layout from '../../components/Layout';
import { useContext } from 'react';
import { useRouter } from 'next/router'
import UserContext from '../../components/UserContext';

const Detail = () => {

    const { getRecipe } = useContext(UserContext);
    const router = useRouter()

    const recipe = getRecipe(router.query.id);

    return (
        <Layout>
            <h1>One of My Things</h1>
            <h2>recipe: {recipe && recipe.title}</h2>
        </Layout>
    );
};

export default Detail;
