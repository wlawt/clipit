import Head from 'next/head'
import styles from '../styles/Home.module.css'
import ReactPlayer from 'react-player'


export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          ClipIt
        </h1>

        {/* <ReactPlayer url="./05012021153052.mp4" controls /> */}
        {/* <div className={styles.videoContainer}>
          <video width="1000" height="500" controls>
            <source src={require("../clips/05012021153052.mp4")} type="video/mp4" />
          </video>
        </div> */}

        {/* width={`"${styles.videoWidth}"`} height={`${styles.videoHeight}`} */}
        <video width="850" controls>
          <source src={require("../clips/05012021153052.mp4")} type="video/mp4" />
        </video>
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
