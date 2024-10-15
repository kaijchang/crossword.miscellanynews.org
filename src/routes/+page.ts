import type { PageLoad } from './$types';
import type { Crossword } from '$lib';
import { env } from '$env/dynamic/public';

import { gql, request } from 'graphql-request';

type CrosswordWithoutData = Omit<Crossword, 'data'>

export const load: PageLoad = async () => {
    const data = await request<{ crosswords: CrosswordWithoutData[] }>(env.PUBLIC_HYGRAPH_API_URL as string, gql`
        {
            crosswords {
                slug
                title
                author {
                    name
                }
                semester
                date
                width
                height
            }
        }
    `);

	return {
        crosswords: data.crosswords,
	};
}
