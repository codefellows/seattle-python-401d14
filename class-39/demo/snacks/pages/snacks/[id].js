export default function SnackDetail(props) {
    return <h1>I am a single snack {props.snack.name}</h1>
}

export async function getServerSideProps(context) {
    const response = await fetch(`http://localhost:3000/api/snacks/${context.params.id}`);
    const snack = await response.json();
    console.log('snack',snack)
    return {
        props: {
            snack
        }
    }
}
