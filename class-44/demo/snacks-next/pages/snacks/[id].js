import { useRouter } from 'next/router'
import axios from 'axios'


export default function SnackDetail(props) {

    const url = 'https://drf-snacks-api.herokuapp.com/api/v1/snacks/';

    const router = useRouter();

    async function deleteHandler() {

        const response = await axios.delete(url + props.snack.id)

        router.push('/');
    }

    return (
        <>
        <h1>I am a single snack {props.snack.name}</h1>
        <button onClick={() => deleteHandler(props.snack.id)}>Delete</button>
        </>
    )
}

export async function getServerSideProps(context) {
    const response = await fetch(`https://drf-snacks-api.herokuapp.com/api/v1/snacks/${context.params.id}`);
    const snack = await response.json();
    console.log('snack',snack)
    return {
        props: {
            snack
        }
    }
}
