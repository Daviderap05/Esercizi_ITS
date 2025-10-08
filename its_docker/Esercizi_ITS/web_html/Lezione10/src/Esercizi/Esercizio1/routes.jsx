import Home from "./Home";
import About from "./About";
import Profiles from "./Profiles";
import SingleProfile from "./SingleProfile";
import MyProfile from "./MyProfile";
import ErrorPage from "./ErrorPage";

export const routes = [

    {
        path:"/",
        element: <Home></Home>
    },
    {
        path:"/about",
        element: <About></About>
    },
    {
        path:"/profiles/",
        element: <Profiles></Profiles>,
        children: [

            {
                path:":id",
                element: <SingleProfile></SingleProfile>
            },
            {
                path:"me",
                element: <MyProfile></MyProfile>
            }
        ]
    },
    {
        path: "*",
        element: <ErrorPage></ErrorPage>
    }
];