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
          Welcome to <a href="https://nextjs.org">Next.js!</a>
        </h1>

        <p className={styles.description}>
          Get started by editing{' '}
          <code className={styles.code}>pages/index.js</code>
        </p>

        <ReactPlayer url="./05012021153052.mp4" controls />
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
