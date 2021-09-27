import './App.css';
import { useQuery } from '@apollo/react-hooks';
import gql from "graphql-tag";

const GET_CHAT = gql`
query{
  chats{
    chat
    id
  }
}
`;

function App() {
  const { data, loading, error } = useQuery(GET_CHAT);
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error</p>;
  return (
    <div className="App">
      {data && data.chats && data.chats.map(chat => (
        <div key={chat.id}><p>{chat.chat}</p></div>
      ))}
    </div>  
  );
}

export default App;
