import type { PageLoad } from './$types';
import type { Crossword } from '../../../@types';
import { env } from '$env/dynamic/public';

import { gql, request } from 'graphql-request';

export const load: PageLoad = async ({ params }) => {
	const { slug } = params;

	const data = await request<{ crossword: Crossword }>(env.PUBLIC_HYGRAPH_API_URL as string, gql`
        query($slug: String!) {
            crossword(where: {
				slug: $slug
			}) {
                slug
                title
                author {
                    name
                }
                semester
                date
                width
                height
				data
            }
        }
    `, { slug });

	return {
		crossword: data.crossword,
	};
}
