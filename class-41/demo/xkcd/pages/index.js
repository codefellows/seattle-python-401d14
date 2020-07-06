import Link from 'next/Link'
import MyLayout from '../components/MyLayout'


export default function Home(props) {
  return (
    <MyLayout>
        <h1>XKCD</h1>
      <h2>{props.comic.title}</h2>
      <img src={props.comic.img} alt={props.comic.alt} />
      <Footer comicNum={props.comic.num} />
    </MyLayout>
  )
}

function Footer(props) {

    const currentNum = props.comicNum;

    const nums = [];

    for(let n = currentNum; n > currentNum - 10; n--) {
        nums.push(n)
    }

return (
    <footer>
        <h2>Previous {nums.length}</h2>
        <ul>
            {nums.map(num => (
                // <li key={num}>
                    <Link href="/num/[id].js" as={`/num/${num}`} key={num}>
                        <a>#{num}</a>
                    </Link>
                // </li>
            ))}
        </ul>
        <style jsx>{`
            a {
                margin-right: 5px;
            }
        `}</style>
    </footer>
)
}

export async function getServerSideProps(context) {

    const response = await fetch('https://xkcd.com/info.0.json');

    const data = await response.json();

    return {
      props: {
          comic: data
      }, // will be passed to the page component as props
    }
  }

