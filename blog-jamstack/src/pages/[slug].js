import { MDXRemote } from "next-mdx-remote";
import { getFileBySlug, getFiles } from "../../lib/mdx";
import MDXComponents from "../../components/MDXComponents";

export default function Post({ sourse, frontmatter }) {
  console.log(sourse);
  return <MDXRemote {...sourse} components={MDXComponents} />;
}

export async function getStaticProps({ params }) {
  const { sourse, frontMatter } = await getFileBySlug(params.slug);
  return {
    props: { sourse, frontMatter },
  };
}

export async function getStaticPaths() {
  const posts = await getFiles();
  const paths = posts.map((post) => ({
    params: {
      slug: post.replace(/\.mdx/, ""),
    },
  }));

  return {
    paths,
    fallback: false,
  };
}
