const rootDiv = document.getElementById("root");
const root = ReactDOM.createRoot(rootDiv);

const App = () => {
  return (
    <>
      <div className="main">
        <h1 className="primo" onClick={(e) => console.log(e)}>
          App
        </h1>

        <Tabella></Tabella>
      </div>
    </>
  );
};

const Tabella = () => {
  return (
    <>
      <ul className="ul">
        <li className="php">PHP</li>
        <li className="js">JS</li>
        <li className="html">HTML</li>
      </ul>
    </>
  );
};

root.render(<App></App>);
