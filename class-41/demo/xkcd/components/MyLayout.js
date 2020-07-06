import Header from './Header';

export default props => (
    <div>
        <Header />
        {props.children}
        <style jsx>{`
            margin: 20px;
            padding: 20px;
            border: 1px solid #DDD;
            background-color: floralwhite;
        `}</style>
    </div>
)
