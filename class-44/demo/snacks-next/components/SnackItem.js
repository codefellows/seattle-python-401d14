
import Link from 'next/link'

export default function SnackItem(props) {
    return (
        <li key={props.snack.id}>
            <Link href="/snacks/[id]" as={`/snacks/${props.snack.id}`}>
                <a>
                    {props.snack.name}
                </a>
            </Link>
        </li>
    )
}
