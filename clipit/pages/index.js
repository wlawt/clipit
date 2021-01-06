import Head from 'next/head'
import styles from '../styles/Home.module.css'
import ReactPlayer from 'react-player'
import React, { useState, useEffect } from 'react'
import Axios from 'axios'

export default function Home() {
  const [fileName, setFileName] = useState("")

  useEffect(() => {
    const getFilename = async () => {
      const name = await Axios.get("http://localhost:3000/api/fileRetriever")

      if (name.status === 200 && name) {
        setFileName(name.data)
      }
    }

    getFilename()
  })

  // console.log(fileName)
  // const file_name = "" + fileName
  // const test = "05012021153052.mp4"

  return (
    <div className={styles.container}>
      <Head>
        <title>ClipIt - Snipping Tool for Videos</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          ClipIt
        </h1>

        <p className="description">Snipping Tool but for Videos 😎</p>

        {/* <div className={styles.videoContainer}>
          <video width="1000" height="500" controls>
            <source src={require("../clips/05012021153052.mp4")} type="video/mp4" />
          </video>
        </div> */}

        {/* width={`"${styles.videoWidth}"`} height={`${styles.videoHeight}`} */}
        {fileName === "" ? (
          <p className="description">No new clip yet!</p>
        ) : (
            <video width="850" controls>
              <source src={require("../clips/" + fileName)} type="video/mp4" />
            </video>
          )}
      </main>

      <footer className={styles.footer}>
        <a
          href="https://twitter.com/wlaw_"
          target="_blank"
          rel="noopener noreferrer"
        >
          Made by <span className={styles.footerText}>William Law</span>
        </a>
      </footer>
    </div>
  )
}