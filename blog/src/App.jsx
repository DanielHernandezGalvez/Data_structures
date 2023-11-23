import { useState } from 'react'
import './App.css'
import {ArticleList, ButtonList} from './Components'
import data from './Components/data/data'

function App() {

  const allCategories = ["All", ...new Set(data.map(article => article.category))]

  const [categories, setCategories] = useState(allCategories)
  const [articles, setArticles] = useState(data)

  const filterCategory = (category) => {
    console.log(category)
  }

  return (
    <>
    <div className="title">
      <h1>filter <span>blog</span> basics</h1>
      <img src="https://blogfilterbasics.netlify.app/static/media/img-portada.8261f3883a73550017d1.png" alt="imagen header" />
    </div>
      <h1>hola mundo</h1>
      <ButtonList categories={categories} filterCategory={filterCategory} />
      <ArticleList articles={articles} />
    </>
  )
}

export default App
